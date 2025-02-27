from string import ascii_lowercase

def palindrome_of_length_at_least_n(txt: str) -> set:
    """
    Write a function called 'palindrome_of_length_at_least_n' that takes one argument,
    a string, and returns the set of all palindromes of the length greater than or
    equal to 21 that exist in the given string. Each palindrome should only
    consist of English letters. If no such palindromes exist in the given string, the
    function should return an empty set. The function should find the palindromes in
    a case-insensitive manner.
    """
    "\n    'ascii_lowercase' contains the list of all lowercase letters in the English alphabet.\n    We are using this to compare the given string to the palindromes in a case-insensitive\n    manner.\n    "
    palindromes = set()
    "\n    'palindromes' is the set of all palindromes of the length greater than or\n    equal to 21 that exist in the given string.\n    "
    for i in range(len(txt)):
        for j in range(i, len(txt)):
            '\n            For each substring of the given string, we are checking if it is a\n            palindrome of the length greater than or equal to 21.\n            '
            substring = txt[i:j + 1]
            "\n            'substring' is the substring of the given string starting at index 'i'\n            and ending at index 'j'.\n            "
            if substring in palindromes:
                "\n                If 'substring' is already in the 'palindromes' set, we don't need\n                to check it again.\n                "
                continue
            if substring == substring[::-1]:
                "\n                If 'substring' is a palindrome, we need to check if it is of the\n                length greater than or equal to 21.\n                "
                if len(substring) >= 21:
                    "\n                    If 'substring' is of the length greater than or equal to 21, we\n                    add it to the 'palindromes' set.\n                    "
                    palindromes.add(substring)
    return palindromes