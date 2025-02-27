def palindromes_of_specific_lengths(s):
    s = s[12:57]
    s = ''.join(filter(str.isalpha, s)).lower()
    result_set = set()
    for i in range(len(s) - 19):
        for length in [20, 21]:
            if i + length <= len(s):
                substring = s[i:i + length]
                if substring == substring[::-1]:
                    result_set.add(s[i:i + length])
    return result_set