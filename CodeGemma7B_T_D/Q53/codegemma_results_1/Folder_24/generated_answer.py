def palindrome_of_length_at_least_n(text):
    """
            Write a function called 'palindrome_of_length_at_least_n' that takes one argument, a string, and returns the set of all palindromes of the length greater than or equal to 53 that exist in the given string. Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
            """
    short_palindromes = {}
    palindrome = ''
    count = 0
    limit = int(len(text) / 2)
    while count <= limit:
        palindrome = text[count] + palindrome
        if palindrome in short_palindromes:
            short_palindromes[palindrome] += 1
        else:
            short_palindromes[palindrome] = 1
        palindrome = palindrome[1:]
        count += 1
    long_palindromes = []
    for key, value in short_palindromes.items():
        if len(key) >= 53:
            long_palindromes.append(key)
    return set(long_palindromes)