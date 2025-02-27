from typing import Set, Union

def palindrome_of_length_at_least_n(string: str) -> Set[str]:
    string = ''.join((c.lower() for c in string if c.isalpha()))
    palindromes = set()
    for i in range(len(string) - 113):
        for j in range(i + 115, len(string), 115):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes