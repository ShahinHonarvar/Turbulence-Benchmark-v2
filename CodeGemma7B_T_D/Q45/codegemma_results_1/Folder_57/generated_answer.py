def palindromes_between_indices(text):
    letters = list(text[2:6].lower())
    palindromes = set()

    def find_palindromes(current_palindrome):
        if len(current_palindrome) == 5:
            palindromes.add(current_palindrome)
            return
        for letter in letters:
            if letter not in current_palindrome:
                current_palindrome.append(letter)
                find_palindromes(current_palindrome)
                current_palindrome.pop()
    find_palindromes([])
    return palindromes