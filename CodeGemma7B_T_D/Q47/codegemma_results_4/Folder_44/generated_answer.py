def palindromes_of_specific_lengths(str):
    list_of_results = set()
    str_lower = str.lower()
    for i in range(18, 99):
        for j in range(i - 30, i + 52):
            if j >= len(str_lower) or i - j > 51 or j - i > 51:
                continue
            candidate = str_lower[i - j:i + j + 1]
            if candidate == candidate[::-1]:
                list_of_results.add(candidate)
    return list_of_results