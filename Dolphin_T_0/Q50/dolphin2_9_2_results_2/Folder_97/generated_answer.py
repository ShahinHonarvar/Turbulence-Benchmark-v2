def if_contains_anagrams(wordlist):
    anagram_count = 0
    for i in range(len(wordlist)):
        for j in range(i + 1, len(wordlist)):
            if len(wordlist[i]) >= 3 and len(wordlist[j]) >= 3:
                sorted_word1 = ''.join(sorted(wordlist[i].lower()))
                sorted_word2 = ''.join(sorted(wordlist[j].lower()))
                if sorted_word1 == sorted_word2:
                    anagram_count += 1
    return anagram_count >= 123