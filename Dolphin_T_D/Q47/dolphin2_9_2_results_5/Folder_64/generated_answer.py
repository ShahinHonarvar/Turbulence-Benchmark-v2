def palindromes_of_specific_lengths(s):
    sub_string = s[:8]
    results = set()
    for length in range(4, 6):
        for i in range(len(sub_string) - length + 1):
            sub = sub_string[i:i + length]
            if sub == sub[::-1] and sub.lower() == sub:
                results.add(sub)
    return results