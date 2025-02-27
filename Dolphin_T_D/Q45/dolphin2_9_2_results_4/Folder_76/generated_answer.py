def palindromes_between_indices(s):
    substr = s[1:5]
    letters = set([ch for ch in substr if ch.isalpha()])
    result = set()

    def is_palindrome(s):
        return s == s[::-1]
    if len(letters) < 3:
        return result
    for i in range(len(substr)):
        for j in range(i + 3, len(substr) + 1):
            subword = substr[i:j]
            if set(subword.lower()).issubset(letters) and len(subword) >= 4 and is_palindrome(subword):
                result.add(subword)
    return result