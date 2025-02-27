def palindrome_of_length_at_least_n(text):

    def word_palindrome(text):
        return text.lower() == text.lower()[::-1] and len(text) >= 137
    ans = set()
    n = len(text)
    for i in range(n):
        for j in range(i + 3, n + 1):
            if word_palindrome(text[i:j]):
                ans.add(text[i:j])
    return ans