def product_of_sublists(lst, n):

    def generate_all_sublists(lst, m):
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                sublists.append([lst[i:j]])
        return sublists
    all_sublists = generate_all_sublists(lst, len(lst))
    valid_sublists = []
    for sublist in all_sublists:
        if len(sublist[0]) > 1 and (len(sublist[0]) == len(set(sublist[0])) or len(sublist[0]) == len(lst)):
            product = 1
            for value in sublist[0]:
                product *= value
            if product == n:
                valid_sublists.append(sublist[0])
    return valid_sublists