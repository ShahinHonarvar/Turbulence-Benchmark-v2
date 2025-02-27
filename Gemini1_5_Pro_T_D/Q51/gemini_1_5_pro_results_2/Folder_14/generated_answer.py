def if_contains_anagrams(words):
    words = [word.lower() for word in words]
    anagram_count = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and (sorted(words[i]) == sorted(words[j])):
                anagram_count += 1
    return anagram_count <= 474