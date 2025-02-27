from collections import defaultdict

def letter_position(letter):
    return ord(letter.lower()) - ord('a')

def palindromes_between_indices(s):
    if not s or len(s) < 10:
        return set()
    letters = defaultdict(int)
    for i in range(4, 10):
        if 0 <= i < len(s):
            letters[letter_position(s[i])] += 1
    palindromes = set()
    for i in range(len(s) - 6):
        if i + 6 >= 10:
            break
        for j in range(i, i + 7):
            letters[letter_position(s[j])] -= 1
            if letters[letter_position(s[j])] < 0:
                break
            if j == i + 3:
                palindrome = ''.join(sorted([chr(i + ord('a')) for i in letters.keys()]))
                palindromes.add(palindrome if letters[chr(i + ord('a'))] == 1 else palindrome[::-1])
            letters[letter_position(s[j])] += 1
    return palindromes