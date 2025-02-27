def palindromes_of_specific_lengths(s):

    def is_palindrome(subs):
        return subs == subs[::-1]

    def filter_non_letters(subs):
        return ''.join((c for c in subs if c.isalpha()))
    s = s[127:289].lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 119, min(start + 142, len(s) + 1)):
            segment = s[start:end]
            clean_segment = filter_non_letters(segment)
            if 119 <= len(clean_segment) <= 141 and is_palindrome(clean_segment):
                palindromes.add(segment)
    return palindromes