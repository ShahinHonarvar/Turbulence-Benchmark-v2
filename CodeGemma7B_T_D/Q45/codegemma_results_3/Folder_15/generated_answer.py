def palindromes_between_indices(text):

    def check_palindrome(text):
        return text == text[::-1]
    palindromes = set()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    for i in range(1, len(text) - 2):
        for j in range(i + 1, len(text) + 1):
            substring = text[i:j]
            if check_palindrome(substring):
                unique_letters = set(substring.lower())
                unique_letters.discard(' ')
                if len(unique_letters) >= 3 and unique_letters & alphabet:
                    palindromes.add(substring)
    return palindromes