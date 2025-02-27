from collections import defaultdict

def palindrome_of_length_at_least_n(str_in):
    str_in = str_in.lower()
    trie = defaultdict(list)
    for i in range(len(str_in) - 11):
        trie[str_in[i]].append(str_in[i:i + 12])
    ans = set()

    def dfs(node, path):
        if len(path) >= 11 and path == path[::-1]:
            ans.add(''.join(path))
        for child in node:
            path.append(child)
            dfs(node[child], path)
            path.pop()
    for letter, node in trie.items():
        path = [letter]
        dfs(node, path)
    return ans