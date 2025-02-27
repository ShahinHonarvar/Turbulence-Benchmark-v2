def palindrome_of_length_at_least_n(n: int, string: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    string = string.lower()
    palindromes = set()
    length = len(string)
    for i in range(length):
        for j in range(i + 149, length):
            sub_string = string[i:j + 1]
            if set(sub_string).issubset(english_letters) and sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    return palindromes