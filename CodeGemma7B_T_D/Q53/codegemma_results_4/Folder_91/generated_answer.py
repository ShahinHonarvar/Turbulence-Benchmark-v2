def palindrome_of_length_at_least_n(string):
    string = string.lower()
    all_palindromes = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            sub = string[i:j]
            if sub == sub[::-1] and len(sub) >= 7:
                all_palindromes.add(sub)
    return all_palindromes