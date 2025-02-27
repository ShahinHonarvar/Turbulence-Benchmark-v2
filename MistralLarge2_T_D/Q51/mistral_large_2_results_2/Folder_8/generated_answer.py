from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    visited = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            for visited_s in visited[sorted_s]:
                if is_anagram(s, visited_s):
                    anagram_count += 1
                    if anagram_count > 68:
                        return False
            visited[sorted_s].append(s)
    return anagram_count <= 68