from collections import defaultdict

def palindrome_of_length_at_least_n(text, n=150):
    """
            This function takes a string and returns the set of all palindromes of the length greater than or equal to n that exist in the given string. Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
            """

    def is_palindrome(word):
        """
                This function checks if a given word is a palindrome in a case-insensitive manner.
                """
        word = word.lower()
        return word == word[::-1]

    def find_palindromes(text):
        """
                This function finds all the palindromes in a given text that are longer than or equal to n.
                """
        palindromes = defaultdict(list)
        for i in range(len(text)):
            for j in range(i + n, len(text) + 1):
                word = text[i:j]
                if is_palindrome(word):
                    palindromes[word].append((i, j))
        return set(palindromes.items())
    return find_palindromes(text.lower())