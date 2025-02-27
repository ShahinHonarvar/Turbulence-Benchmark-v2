def palindrome_of_length_at_least_n(text):
    """
            Write a function called 'palindrome_of_length_at_least_n' that takes one argument, a string, and returns the set of all palindromes of the length greater than or equal to 86 that exist in the given string. Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
            """
    for i in range(len(text)):
        for j in range(i + 42, len(text)):
            temp = text[i:j + 1]
            if temp == temp[::-1] and temp.isalpha():
                yield temp
    else:
        yield from ()