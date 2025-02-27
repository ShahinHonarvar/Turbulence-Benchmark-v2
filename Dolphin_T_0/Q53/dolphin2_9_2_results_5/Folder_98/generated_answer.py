def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    length = len(s)
    for length_of_palindrome in range(6, length + 1):
        for i in range(0, length_of_palindrome):
            temp_word = s[i:i + length_of_palindrome]
            if temp_word == temp_word[::-1]:
                result.add(temp_word)
    return result