def palindromes_of_specific_lengths(s):
    start, end = (62, 88)
    min_length, max_length = (18, 21)
    s = s[start:end + 1]
    palindromes = set()
    for i in range(len(s)):
        for length in range(min_length, max_length + 1):
            if i + length <= len(s):
                sub = s[i:i + length]
                sub_letters_only = ''.join((c for c in sub if c.isalpha()))
                if len(sub_letters_only) == length and sub_letters_only.lower() == sub_letters_only[::-1].lower():
                    palindromes.add(sub_letters_only)
    return palindromes