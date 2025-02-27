def palindromes_between_indices(s):
    letters = s[2:5]
    flat_letters = set(''.join(letters))
    flat_letters = flat_letters.intersection(set('abcdefghijklmnopqrstuvwxyz'))
    all_palindromes = set()
    for letter in flat_letters:
        for i in range(len(letters), 2, -1):
            for j in range(2 ** i):
                palindrome = ''.join((flat_letters.pop(0) for _ in range(i)))
                if palindrome == palindrome[::-1] and i >= 3:
                    all_palindromes.add(palindrome)
    return all_palindromes