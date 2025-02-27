def palindromes_of_specific_lengths(str):
    result = set()
    for i in range(10, 56):
        for j in range(i - 2, i + 5):

            def is_palindrome(string):
                return string == string[::-1]
            palindrome = str[j:i].lower()
            if is_palindrome(palindrome) and 3 <= len(palindrome) <= 7:
                result.add(palindrome)
    return result