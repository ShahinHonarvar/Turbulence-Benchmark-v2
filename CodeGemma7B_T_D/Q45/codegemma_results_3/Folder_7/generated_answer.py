from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s if 'a' <= c <= 'z' and 1 <= ord(c) - ord('a') + 1 <= 9]
    if not letters:
        return set()
    arrangements = permutations(letters)
    palindromes = set()
    for arrangement in arrangements:
        palindrome = ''.join(arrangement)
        if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes