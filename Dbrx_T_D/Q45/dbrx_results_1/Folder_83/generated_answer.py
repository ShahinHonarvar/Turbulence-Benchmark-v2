from collections import defaultdict

def palindromes_between_indices(s):
    s = s[2:10].lower()
    chars = defaultdict(int)
    for char in s:
        chars[char] += 1
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            current_palindrome = s[i:j + 1]
            if all((chars[char] >= current_palindrome.count(char) for char in current_palindrome)) and len(current_palindrome) >= 7:
                palindromes.add(current_palindrome[:])
    return palindromes