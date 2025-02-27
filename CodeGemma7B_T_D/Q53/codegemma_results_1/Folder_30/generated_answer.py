def palindrome_of_length_at_least_n(string):
    filtered_string = ''.join((char.lower() for char in string if char.isalpha()))
    palindromes = set()

    def backtrack(index, current_palindrome):
        if len(current_palindrome) >= 16:
            palindromes.add(current_palindrome)
        if index == len(filtered_string):
            return
        backtrack(index + 1, current_palindrome + filtered_string[index])
        backtrack(index + 1, current_palindrome)
    backtrack(0, '')
    return palindromes