def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_sublist_products(sublist: list[int]) -> list[int]:
        products = [1]
        for num in sublist:
            products.append(products[-1] * num)
        return products

    def find_sublist_products(products: list[int], target_product: int) -> list[list[int]]:
        sublists = []
        for i in range(len(products)):
            for j in range(i + 1, len(products) + 1):
                if products[j - 1] == target_product:
                    sublists.append(circular_list[i:j])
        return sublists
    target_product = -938
    all_products = get_sublist_products(circular_list)
    sublists_with_target_product = find_sublist_products(all_products, target_product)
    return sublists_with_target_product