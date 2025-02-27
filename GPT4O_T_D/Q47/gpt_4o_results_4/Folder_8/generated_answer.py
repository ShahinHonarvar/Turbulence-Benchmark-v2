def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[17:73].lower()
    allowed_chars = set('abcdefghijklmnopqrstuvwxyz')
    substrings = set()
    for start in range(len(s)):
        for length in [50, 51]:
            end = start + length
            if end > len(s):
                continue
            current_sub = ''.join([c for c in s[start:end] if c in allowed_chars])
            if len(current_sub) in [50, 51] and is_palindrome(current_sub):
                substrings.add(current_sub)
    return substrings