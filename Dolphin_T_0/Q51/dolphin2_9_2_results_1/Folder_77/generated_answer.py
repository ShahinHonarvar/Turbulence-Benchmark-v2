from collections import defaultdict

def if_contains_anagrams(l1):
    count = 0
    graph = defaultdict(list)
    for s in l1:
        key = ''.join(sorted(s)).lower()
        graph[key].append(s)
    for key in graph:
        n = len(graph[key])
        if n >= 2:
            count += n * (n - 1) // 2
    return count <= 17