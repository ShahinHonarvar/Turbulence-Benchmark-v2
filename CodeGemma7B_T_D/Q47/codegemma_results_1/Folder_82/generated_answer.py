def palindromes_of_specific_lengths(text):

    class PalindromeFinder:

        def __init__(self):
            self.palindromes = set()

        def find_palindromes(self, txt, start, end):
            for length in range(30, 301):
                for i in range(start, end - length + 1):
                    substring = txt[i:i + length]
                    if substring == substring[::-1].lower():
                        self.palindromes.add(substring)
    palindrome_finder = PalindromeFinder()
    palindrome_finder.find_palindromes(text.lower(), 3, 300)
    return palindrome_finder.palindromes