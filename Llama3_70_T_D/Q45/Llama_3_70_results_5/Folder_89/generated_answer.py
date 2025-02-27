def palindromes_between_indices(s):
    s = s[5:10].lower()
    chars = sorted(list(set(s)))
    anagrams = set()

    def generate_anagrams(anagram, remaining_chars):
        if len(anagram) >= 6:
            anagrams.add(anagram)
        for i in range(len(remaining_chars)):
            generate_anagrams(anagram + remaining_chars[i], remaining_chars[:i] + remaining_chars[i + 1:])
    generate_anagrams('', chars)
    return {anagram for anagram in anagrams if anagram == anagram[::-1]}