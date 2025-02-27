def palindromes_of_specific_lengths(s):
    s_substring = s[11:84]
    palmondromes = set()
    for length in range(37, 61):
        for i in range(len(s_substring) - length + 1):
            sub_string = s_substring[i:i + length]
            if sub_string.lower() == sub_string[::-1].lower():
                palmondromes.add(sub_string)
    return palmondromes