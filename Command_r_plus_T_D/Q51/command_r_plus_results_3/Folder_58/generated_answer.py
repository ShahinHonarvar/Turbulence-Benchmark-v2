def if_contains_anagrams(lst):

    def normalize_text(text):
        return text.lower()

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            str1, str2 = (normalize_text(lst[i]), normalize_text(lst[j]))
            if len(str1) >= 3 and len(str2) >= 3 and is_anagram(str1, str2):
                anagram_count += 1
                if anagram_count > 60:
                    return False
    return True