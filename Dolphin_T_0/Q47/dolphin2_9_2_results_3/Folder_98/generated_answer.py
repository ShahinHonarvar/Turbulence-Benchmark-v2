def palindromes_of_specific_lengths(s):
    result_set = set()
    for length in range(5, 81):
        s = s.lower()
        for start_index in range(0, 21):
            substring = s[start_index:start_index + length]
            if substring == substring[::-1]:
                if substring.isalpha():
                    result_set.add(substring)
    return result_set