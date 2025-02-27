def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(29, 97):
        for length in range(12, 19):
            end_index = i + length - 1
            if end_index < len(s):
                sub_s = s[i:end_index + 1].lower()
                if sub_s == sub_s[::-1] and sub_s.isalpha():
                    palindromes.add(sub_s[::-1])
    return palindromes