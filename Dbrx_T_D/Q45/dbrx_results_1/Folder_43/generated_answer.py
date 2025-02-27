import string

def palindromes_between_indices(s):
    english_letters = string.ascii_letters
    palindromes = set()
    start_index = 2
    end_index = 5
    substring = s[start_index:end_index + 1].lower()
    letters_in_range = set(english_letters).intersection(set(substring))
    if len(letters_in_range) < 2:
        return palindromes
    for length in range(4, len(letters_in_range) + 1):
        for combination in itertools.combinations(letters_in_range, length):
            if len(combination) < 2:
                continue
            combination = ''.join(combination)
            palindrome = ''
            for i in range(len(combination)):
                palindrome += combination[i]
                if combination[i:].startswith(palindrome) and palindrome[::-1] == palindrome:
                    palindromes.add(palindrome)
    return palindromes