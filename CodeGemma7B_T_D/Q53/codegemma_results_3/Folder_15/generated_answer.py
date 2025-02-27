def palindrome_of_length_at_least_n(string_):
    for i in range(len(string_)):
        for j in range(i + 4, len(string_) + 1):
            substring = string_[i:j]
            if substring == substring[::-1]:
                set_of_palindromes.add(substring.lower())
    return set_of_palindromes