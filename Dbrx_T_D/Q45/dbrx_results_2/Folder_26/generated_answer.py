from sets import Set

def palindromes_between_indices(s):
    palindromes = Set()
    english_letters = Set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    start_index = 4
    end_index = 6
    for i in range(start_index, end_index + 1):
        for j in range(i, end_index + 1):
            substring = s[i:j + 1]
            if all((c in english_letters for c in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes