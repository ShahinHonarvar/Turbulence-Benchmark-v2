def palindromes_of_specific_lengths(s):
    valid_chars = 'abcdefghijklmnopqrstuvwxyz'
    substr = s[124:284].lower()
    palindromes = set()
    for length in range(115, 135):
        for i in range(len(substr) - length + 1):
            sub_str = substr[i:i + length]
            filtered_str = ''.join(filter(lambda c: c in valid_chars, sub_str))
            if len(filtered_str) == length and filtered_str == filtered_str[::-1]:
                palindromes.add(filtered_str)
    return palindromes