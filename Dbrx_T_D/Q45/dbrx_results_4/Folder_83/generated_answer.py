from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    result = set()
    for i in range(2, 10):
        for j in range(i, 10):
            substr = s[i:j + 1].lower()
            if len(substr) < 7 or not substr.isalpha():
                continue
            freq = defaultdict(int)
            for char in substr:
                freq[char] += 1
            if all((freq[char] % 2 == 0 for char in freq)) or len(set(freq.values()) - set([1])) < 1:
                result.add(''.join((ch * (count // 2) for ch, count in sorted(freq.items()))))
    return result