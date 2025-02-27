from collections import Counter

def if_contains_anagrams(words):
    anagram_count = 0
    processed_words = [''.join(sorted(word.lower())) for word in words]
    considered_pairs = set()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                if processed_words[i] == processed_words[j]:
                    pair = tuple(sorted((words[i].lower(), words[j].lower())))
                    if pair not in considered_pairs:
                        considered_pairs.add(pair)
                        anagram_count += 1
                        if anagram_count > 89:
                            return False
    return True