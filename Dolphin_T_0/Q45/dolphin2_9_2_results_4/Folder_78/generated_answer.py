def palindromes_between_indices(s):
    letters = s[6:9]
    chars = [c.lower() for c in set(letters) if c.isalpha()]

    def is_palindrome(s):
        return s == s[::-1]
    result = set()
    for i in range(len(chars)):
        for j in range(i + 2, len(chars) + 1):
            subs = ''.join(chars[i:j])
            if is_palindrome(subs):
                result.add(subs)
    return result