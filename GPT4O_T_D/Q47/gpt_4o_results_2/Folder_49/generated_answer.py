def palindromes_of_specific_lengths(string):

    def is_palindrome(s):
        filtered = [ch for ch in s if ch.isalpha()]
        return filtered == filtered[::-1]
    string = string.lower()
    palindromes = set()
    for start in range(10, 101):
        for end in range(start + 10, min(start + 51, 101)):
            substring = string[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes