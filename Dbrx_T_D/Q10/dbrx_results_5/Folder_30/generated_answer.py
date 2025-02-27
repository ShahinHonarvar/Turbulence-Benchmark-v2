def all_odd_ints_exclusive(numbers):
    startIndex = 86
    endIndex = 89
    result = []
    if startIndex < 0 or startIndex >= len(numbers) or endIndex < 0 or (endIndex > len(numbers)):
        return result
    for i in range(startIndex, endIndex):
        if numbers[i] % 2 != 0:
            result.append(numbers[i])
    return result