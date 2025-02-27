def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]

    def extract_letters(sub):
        return ''.join((c for c in sub if c.isalpha()))
    s_sub = s[31:75]
    result = set()
    for start in range(0, len(s_sub)):
        for end in range(start + 23, min(len(s_sub), start + 40)):
            sub = s_sub[start:end + 1]
            letters = extract_letters(sub).lower()
            if 23 <= len(letters) <= 39 and is_palindrome(letters):
                result.add(sub)
    return result