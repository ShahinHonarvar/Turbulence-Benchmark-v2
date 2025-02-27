def palindromes_between_indices(s):
    letters = [c for c in s[3:9] if 'a' <= c.lower() <= 'z']
    palindromes = set()

    def is_palindrome(words):
        return words == words[::-1]
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            sub = ''.join(letters[i:j])
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes