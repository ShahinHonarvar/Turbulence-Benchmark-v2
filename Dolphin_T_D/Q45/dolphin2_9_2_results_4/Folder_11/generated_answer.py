def palindromes_between_indices(given_string):
    substring = given_string[2:7]
    substring = ''.join((c for c in substring if c.isalpha()))
    all_palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            sub_string_palindrome = substring[i:j]
            if sub_string_palindrome == sub_string_palindrome[::-1]:
                all_palindromes.add(sub_string_palindrome.lower())
    return all_palindromes