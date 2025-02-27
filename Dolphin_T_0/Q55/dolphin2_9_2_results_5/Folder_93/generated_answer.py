def lists_with_product_equal_n(numbers):
    result = []
    if len(numbers) == 0:
        return []
    if len(numbers) == 1:
        return [numbers] if numbers[0] == -91 else []
    for i in range(len(numbers)):
        current = numbers[i]
        if current == -91:
            result.append([numbers[i]])
        for j in range(i + 1, len(numbers)):
            current *= numbers[j]
            if current == -91:
                result.append(numbers[i:j + 1])
            if current > -91:
                break
    return result