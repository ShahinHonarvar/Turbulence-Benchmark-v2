import re
    from collections import defaultdict

def palindromes_between_indices(s):
    pattern = re.compile('[^a-zA-Z]')
    s = pattern.sub('', s)
    letters = s[2:8].lower()
    letter_count = defaultdict(int)
    for letter in letters:
        letter_count[letter] += 1
    odd_count_letters = [letter for letter in letter_count if letter_count[letter] % 2 != 0]
    for letter in odd_count_letters:
        letter_count[letter] //= 2
    palindromes = set()
    for i in range(1, 27):
        for j in range(i, 27):
            if sum((letter_count[chr(i + 96)] + letter_count[chr(j + 96)] for i, j in zip(range(1, 27, 2), range(2, 28, 2)))) < 3:
                continue
            palindrome = ''.join([chr(i + 96) * letter_count[chr(i + 96)] + chr(j + 96) * letter_count[chr(j + 96)] for i, j in zip(range(1, 27, 2), range(2, 28, 2))])
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes