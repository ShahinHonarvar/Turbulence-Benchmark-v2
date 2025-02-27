def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(1, 8):
        for j in range(i + 2, 8):
            substring = s[i:j + 1]
            lower_substring = substring.lower()
            if set(lower_substring).issubset('abcdefghijklmnopqrstuvwxyz'):
                if len(substring) in [3, 4] and substring == substring[::-1]:
                    result.add(substring)
    return result