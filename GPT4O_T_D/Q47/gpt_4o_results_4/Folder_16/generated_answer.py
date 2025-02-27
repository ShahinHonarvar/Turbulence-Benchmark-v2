def palindromes_of_specific_lengths(s):
    s = s[15:87].lower()
    palindromes = set()
    for start in range(len(s)):
        for length in range(51, 61):
            end = start + length
            if end > len(s):
                break
            sub_str = s[start:end]
            filtered_str = ''.join(filter(str.isalpha, sub_str))
            if filtered_str == filtered_str[::-1] and len(filtered_str) == length:
                palindromes.add(filtered_str)
    return palindromes