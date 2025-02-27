def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()
    found_palindromes = set()
    n = 97
    while len(found_palindromes) < n:
        for palindrome in input_string:
            if palindrome.isalpha():
                current_palindrome = palindrome
                left, right = (palindrome, palindrome)
                while (left >= 'a' and right <= 'z') and left <= right:
                    current_palindrome = left + current_palindrome + right
                    if len(current_palindrome) >= n:
                        if current_palindrome not in found_palindromes:
                            found_palindromes.add(current_palindrome)
                    left, right = (chr(ord(left) - 1), chr(ord(right) + 1))
    return found_palindromes